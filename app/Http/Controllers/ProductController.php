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
    	$product = Product::find($id);
        $add = "add".$id;
        $quantity = $request->input($add);
    	
        if ($product->inStock > 0 && $quantity  < $product->inStock)
    	{
    		$oldCart = Session::has('cart')?Session::get('cart'):null;
            
        

            $cart = new Cart($oldCart);
            $cart->add($product, $product->id, $quantity);

            $product->inStock = $product->inStock - $quantity;

            $request->session()->put('cart', $cart);

            $product->save();    

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

       if(!Auth::check())
            return redirect()->route('user.signin');    
        
        Auth::user()->orders()->save($order);

        Session::forget('cart');
        return redirect()->route('product.index')->with('success', 'Successfully purchased products!');
    }

    public function getRemoveOne(Request $request, $id)
    {
        $oldCart = Session::has('cart')?Session::get('cart'):null;
        $cart = new Cart($oldCart);
        $product = Product::find($id);
        $product->inStock += 1;
        $product->save();
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
        $product->inStock += $cart->items[$id]['Qty'];
        $product->save();
        $cart->removeAll($id);

        Session()->put('cart', $cart);

        $oldCart = Session::get('cart');
        $cart = new Cart($oldCart);
        $totalPrice = $cart->totalPrice;

        if($totalPrice <= 0.0) Session::forget('cart');
        return view('user.shopping-cart', ['products' => $cart->items, 'totalPrice' => $totalPrice]);
    }
}
