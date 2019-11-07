@extends('admin.layouts.master')

@section('title')
	Administrator
@endsection

@section('content')
<div class="btn-group btn-group-justified" role="group" aria-label="...">
  <div class="btn-group" role="group">
    <a href="{{route('addproduct')}}" type="button" class="btn btn-default"> Add Product </a>
  </div>
  <div class="btn-group" role="group">
     <a href="{{route('updateproduct')}}" type="button" class="btn btn-default"> Update Product </a>
  </div>
  <div class="btn-group" role="group">
    <a type="button" class="btn btn-default"> Customer </a>
  </div>
  <div class="btn-group" role="group">
    <a type="button" class="btn btn-default"> Report Orders </a>
  </div>
</div>
@endsection