@extends('admin.layouts.master')
@section('title')
	Admin
@endsection

@section('content')
<form action="{{ route('postupdateproduct') }}" method="POST" enctype="multipart/form-data">
    <div class="form-group" hidden="True">
      <label for="id"> ID </label>
      <input style="width: 600px" type="text" id="id" name="id" value="{{$product->id}}"></input>
    </div>
    <div class="form-group">
      <label for="title"> Title </label>
      <input style="width: 600px" type="text" id="title" name="title" placeholder="{{$product->title}}" pattern="(?=.*[0-9a-zA-Z]).{1,20}"></input>
    </div>
    <div class="form-group">
      <label for="author"> Author </label>
      <input type="text" id="author" name="author" placeholder="{{$product->author}}" pattern="(?=.*[0-9a-zA-Z]).{1,20}"></input>
    </div>
    <div class="form-group">
      <label for="price"> Price </label>
      <input type="text" id="price" name="price" placeholder="{{$product->price}}" pattern="[0-9]+(\.[0-9][0-9]?)"'></input>
    </div>
    <div class="form-group">
      <label for="in-stock"> In stock: </label>
      <input type="number" id="in-stock" name="in-stock" placeholder="{{$product->inStock}}"></input>
    </div>
    <div class="form-group">
       <label for="description"> Description </label>
          <textarea id = "description"
                  name = "description"
                  rows = "3"
                  cols = "80" placeholder="{{$product->description}}"></textarea>
    </div>
    <div class="form-group"> 
      <label for="imageProduct"> Image of Product </label>
      <input type="file" id="imageProduct" name="imageProduct">
    </div>
   
    <button type="submit" class="btn btn-primary"> Save </button>
    {{ csrf_field() }}
  </form>
@endsection