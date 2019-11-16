@extends('admin.layouts.master')

@section('title')
	Admin
@endsection

@section('content')
	@foreach($products->chunk(3) as $productChunk)
  <div class="row">
    @foreach($productChunk as $product)
  <div class="col-sm-6 col-md-4">
    <div class="thumbnail">
      <img src="{{$product->imagePath}}" alt="...">
      <div class="caption">
        <h3>{{$product->title}} ({{$product->author}})</h3>
        <p class="description">{{$product->description}}
        </p>
       
          <div class="clearfix">
            <div class="pull-left price">In Stock: {{$product->inStock}} </div>
          </div>
          <div class="clearfix">
          <div class="pull-left price"> {{$product->price}}$ </div>
               <a href="{{route('product.updateproduct', ['id' => $product->id])}}" type="button" class="btn btn-success pull-right">Update this</a>
          </div>
        </div>
        </div>
      </div>
      @endforeach
    </div>
	@endforeach
@endsection