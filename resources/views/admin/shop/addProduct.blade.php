@extends('admin.layouts.master')

@section('title')
shopping cart
@endsection

@section('content')
  <form action="{{ route('addproduct') }}" method="POST" enctype="multipart/form-data">
    <div class="form-group">
      <label for="title"> Title </label>
      <input type="text" id="title" name="title" pattern="(?=.*[0-9a-zA-Z]).{1,20}" required></input>
    </div>
    <div class="form-group">
      <label for="author"> Author </label>
      <input type="text" id="author" name="author" pattern="(?=.*[0-9a-zA-Z]).{1,20}" required></input>
    </div>
    <div class="form-group">
      <label for="price"> Price </label>
      <input type="text" id="price" name="price" pattern='[0-9]+(\.[0-9][0-9]?)?' title="2.34 (just two or one number after dot) or 2 or 2.1" required></input>
    </div>
    <div class="form-group">
      <label for="in-stock"> In stock: </label>
      <input type="number" id="in-stock" name="in-stock" required></input>
    </div>
    <div class="form-group">
       <label for="description"> Description </label>
          <textarea id = "description"
                  name = "description"
                  rows = "3"
                  cols = "80" placeholder="Your text here" required></textarea>
    </div>
    <div class="form-group"> 
      <label for="imageProduct"> Image of Product </label>
      <input type="file" id="imageProduct" name="imageProduct"></input>
    </div>
   
    <button type="submit" class="btn btn-primary"> Add product </button>
    {{ csrf_field() }}
  </form>
@endsection