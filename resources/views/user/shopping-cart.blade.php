@extends('layouts.master')

@section('title')
LS BookStore
@endsection

@section('content')
  @if(Session::has('cart'))
    <div class="row">
        <div class="col-sm-6 col-md-6 col-md-offset-3 col-sm-offset-3">
          <ul class="list-group">
            @foreach($products as $product)
                <li class="list-group-item">
                  <span class="badge">{{ $product['Qty'] }}</span>
                  <strong>{{ $product['item']['title'] }}</strong>
                  <span class="label label-success">{{ $product['price'] }}$</span>
                  <div class="btn-group">
                     <a href="{{route('product.removeall', ['id' => $product['id']])}}" type="button" class="btn btn-primary btn-xs">
                      Remove all</a>
                     <a href="{{route('product.removeone', ['id' => $product['id']])}}" type="button" class="btn btn-primary btn-xs">
                      Remove 1</a>
                  </div>                
                </li>
            @endforeach
          </ul>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-6 col-md-6 col-md-offset-3 col-sm-offset-3">
          <strong>total: {{$totalPrice}}$</strong>
        </div>
        <div class="col-sm-6 col-md-6 col-md-offset-3 col-sm-offset-3">
            <a href="{{route('product.checkout')}}" type="button" class="btn btn-primary btn-success">
                      Checkout</a>
        </div>
    </div>
  @else
  <div class="row">
        <div class="col-sm-6 col-md-6 col-md-offset-3 col-sm-offset-3">
          <h2>No item in cart!</h2>
        </div>
    </div>
  @endif
@endsection