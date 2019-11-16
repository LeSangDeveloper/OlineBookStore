@extends('layouts.master')

@section('title')
LS BookStore
@endsection

@section('content')
<div class="row">
  <div class="col-sm-6 col-md-4 col-md-offset-4 col-sm-offset-3">
    <form action="{{route('product.checkout')}}" method="post" id="checkout-form">
    	<div class="row">
    		<div class="col-sx-12">
    			<div class="form-group">
    				<label for="name">Name</label>
    				<input type="text" id="name" class="form-control" name="name-order" pattern="(?=.*[A-Z])(?!.*[0-9]).{2,}" title ="John D. or Lee Shang" required>
    			</div>
    		</div>
    		<div class="col-sx-12">
    			<div class="form-group">
    				<label for="address">Address</label>
    				<input type="text" id="address" class="form-control" pattern="(?=.*[a-Z0-9A-Z]).{2,}" required>
    			</div>
    		</div>
    		<div class="col-sx-12">
    			<div class="form-group">
    				<label for="number-phone">Number phone:</label>
    				<input type="number" id="number-phone" class="form-control" name="address" required>
    			</div>
    		</div>
    	</div>
    	{{	csrf_field() }}
    	<button type="submit" class="btn btn-primary btn-success" name="buy"> Buy now </button>
    </form>
  </div>
</div>
@endsection