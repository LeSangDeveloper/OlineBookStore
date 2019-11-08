<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Product;
use App\Http\Requests;
use Intervention\Image\Facades\Image;
use DB;
use Auth;

class AdminController extends Controller
{
    //
    public function getIndex()
	{
		return view('admin.index');
	}

	public function getAddProduct()
	{
		return view('admin.shop.addProduct');
	}

	public function postAddProduct(Request $request)
	{
		$imageProduct = $request->file('imageProduct');
		$order = DB::table('products')->max('id');
		$product = new Product;
		$product->title = $request->input('title');
		$product->author = $request->input('author');
		$product->description = $request->input('description');
		$product->inStock = (int)$request->input('in-stock');
		$product->price = (float)$request->input('price');
		$filename = 'th' . $order . '.png';
		$product->imagePath = "public/src/images/th" . $order . '.png';
		Image::make($request->imageProduct->getRealPath())->resize(300, 300)->save( public_path('\src\images\\' . $filename));
		Image::make($request->imageProduct->getRealPath())->resize(300, 300)->save( 'admin\public\src\images\\' . $filename);
		Image::make($request->imageProduct->getRealPath())->resize(300, 300)->save( 'admin\updateProduct\public\src\images\\' . $filename);
		Image::make($request->imageProduct->getRealPath())->resize(300, 300)->save( 'user\add-to-cart\public\src\images\\' . $filename);
		$product->save();
		return view('admin.index');
	}

	public function getUpdateProduct()
	{
		$products = Product::all();
    	return view('admin.shop.updateProduct', ['products' => $products]);
	}

	public function postUpdateProduct(Request $request)
	{
		$product = Product::find($request->input('id'));
		if ($request->input('title') != '')
		{
			$product->title = $request->input('title');
		}
		if ($request->input('author') != '')
		{
			$product->author = $request->input('author');
		}
		if ($request->input('price') != '')
		{
			$product->price = $request->input('price');
		}
		if ($request->input('description') != '')
		{
			$product->description = $request->input('description');
		}   	
		if ($request->input('in-stock') != '')
		{
			$product->inStock = $request->input('in-stock');
		}
		$product->save();
		$products = Product::all();
		return view('admin.shop.updateProduct', ['products' => $products]);
	}

	public function getUpdateProductId($id)
	{
		$product = Product::find($id);
    	return view('admin.shop.formUpdate', ['product' => $product]);
	}
}
