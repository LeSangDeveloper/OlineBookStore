<?php

namespace App\Http\Controllers;

use App\Product;

use App\Cart;

use Illuminate\Http\Request;

use App\Http\Requests;

use Session;

class ProductController extends Controller
{
    //
    public function getIndex()
    {
    	$products = Product::all();
    	return view('shop.index', ['products' => $products]);
 
    }

    public function getAddToCart(Request $request, $id)
    {
    	$product = Product::find($id);
    	if ($product->inStock > 0)
    	{
    		$product->inStock -= 1;
    		$oldCart = Session::has('cart')?Session::get('cart'):null;
    	
    		$cart = new Cart($oldCart);
    		$cart->add($product, $product->id);

    		$request->session()->put('cart', $cart);
    		$product->save();
    		return redirect()->route('product.index');
		}
		else 
			return redirect()->route('product.index');
	}
}
