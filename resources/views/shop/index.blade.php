@extends('layouts.master')

@section('title')
LS Bookstore
@endsection

@if(!$search)
@section('content')

@if(Session::has('success'))
  <div class="row">
  <div class="col-sm-6 col-md-4">
    <div id="charge-message" class="alert alert-success">
        {{ Session::get('success') }}
    </div>
  </div>
</div> 
@endif

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
          @if($product->inStock > 0)
          <form action="{{route('product.addToCart', ['id'=>$product->id])}}" method="post">
             <div class="form-group pull-right" style="max-width: 60px">
              <input type="number" class="form-control" name="add{{$product->id}}" placeholder="Num" required>
               <button type="submit" class="btn btn-success pull-right">Add to cart</button>
              {{ csrf_field() }}
              </div>
          </form>
          @else
          <a href="#" class="btn btn-danger pull-right" role="button">Out of stock !</a>
          @endif
        </div>
      </div>
    </div>
  </div>
  @endforeach
</div>

@endforeach
@endsection

@else
@section('content')
    @foreach($products as $product)
  <div class="col-sm-6 col-md-4">
    <div class="thumbnail">
      <img src="{{$product->imagePath}}" alt="...">
      <div class="caption">
        <h3>{{$product->title}}</h3>
        <p class="description">{{$product->description}}
        </p>
         <div class="clearfix">
            <div class="pull-left price">In Stock: {{$product->inStock}} </div>
        </div>
        <div class="clearfix">
         
          <div class="pull-left price"> {{$product->price}}$ </div>
           @if($product->inStock > 0)
          <form action="{{route('product.addToCart', ['id'=>$product->id])}}" method="post">
             <div class="form-group pull-right" style="max-width: 60px">
              <input type="number" class="form-control" name="add{{$product->id}}" placeholder="Num">
               <button type="submit" class="btn btn-success pull-right">Add to cart</button>
              {{ csrf_field() }}
              </div>
          </form>
          @else
          <a href="#" class="btn btn-danger pull-right" role="button">Out of stock !</a>
          @endif
        </div>
      </div>
    </div>
  </div>
  @endforeach
</div>
@endsection
@endif