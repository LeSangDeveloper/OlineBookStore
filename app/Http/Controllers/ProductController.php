<?php

namespace App\Http\Controllers;

use App\Product;

use App\Cart;

use App\Order;

use Illuminate\Http\Request;

use App\Http\Requests;

use DB;

use Auth;

use Session;

class ProductController extends Controller
{
    //
    public function getIndex()
    {
    	$products = Product::all();
    	return view('shop.index', ['products' => $products, 'search' => false]);
 
    }

    public function postIndex(Request $request)
    {   
        $inp = $request->input('search');
        $inp = '%'. $inp .'%';
        $products = DB::table("products")->where('products.title', 'LIKE', $inp)->get();
        Session::put('search', $products);
        return view('shop.index', ['products' => $products, 'search' => true]);
    }

    public function postAddToCart(Request $request, $id)
    {

        $add = "add".$id;
        $quantity = $request->input($add);
    	$product = Product::find($id);
        if ($product->inStock > 0 && $quantity  <= $product->inStock)
    	{
    		$oldCart = Session::has('cart')?Session::get('cart'):null;
            
        

            $cart = new Cart($oldCart);
            $cart->add($product, $product->id, $quantity);



            $request->session()->put('cart', $cart);

   

            $products = Product::all();
            return view('shop.index', ['products' => $products, 'search' => false]);
		}
		else 
			return redirect()->route('product.index');
	}

    public function getShoppingCart()
    {
        if (!Session::has('cart'))
            return view('user.shopping-cart');

        $oldCart = Session::get('cart');
        $cart = new Cart($oldCart);
        $totalPrice = $cart->totalPrice;
        return view('user.shopping-cart', ['products' => $cart->items, 'totalPrice' => $totalPrice]);
    }

    public function getCheckout()
    {
        return view('user.checkout');
    }

    public function postCheckout(Request $request)
    {
                if(!Session::has('cart'))
        {
            return view('shop.index');
        }
        
        $oldCart = Session::get('cart');
        $cart = new Cart($oldCart);
        
        $order = new Order();
        $order->cart = serialize($cart);
        $order->name = $request->input('name-order');
        $order->address = $request->input('address');

        foreach($cart->items as $item)
        {
            $product = Product::find($item['id']);
            if ($product->inStock >= $item['Qty'])
            {
                $product->inStock = $product->inStock - $item['Qty'];
                 
            }
            else
                return redirect()->route('product.index')->with('success', 'Product Purchased failed! '. title . 'just have only'. $product->inStock .'in stock!');
        }
        
       if(!Auth::check())
            return redirect()->route('user.signin');    
        
        $product->save();
        Auth::user()->orders()->save($order);

        Session::forget('cart');
        return redirect()->route('product.index')->with('success', 'Successfully purchased products!');
    }

    public function getRemoveOne(Request $request, $id)
    {
        $oldCart = Session::has('cart')?Session::get('cart'):null;
        $cart = new Cart($oldCart);
        $product = Product::find($id);
        $cart->removeOne($id);

        Session()->put('cart', $cart);

        $oldCart = Session::get('cart');
        $cart = new Cart($oldCart);
        $totalPrice = $cart->totalPrice;

        if($totalPrice <= 0.0) Session::forget('cart');
        return view('user.shopping-cart', ['products' => $cart->items, 'totalPrice' => $totalPrice]);
    }

    public function getRemoveAll(Request $request, $id)
    {
        $oldCart = Session::has('cart')?Session::get('cart'):null;
        $cart = new Cart($oldCart);
        $product = Product::find($id);
        $cart->removeAll($id);

        Session()->put('cart', $cart);

        $oldCart = Session::get('cart');
        $cart = new Cart($oldCart);
        $totalPrice = $cart->totalPrice;

        if($totalPrice <= 0.0) Session::forget('cart');
            return view('user.shopping-cart', ['products' => $cart->items, 'totalPrice' => $totalPrice]);
    }
}
