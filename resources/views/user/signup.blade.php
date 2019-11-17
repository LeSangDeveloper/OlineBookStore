@extends('layouts.master')

@section('title')
LS BookStore
@endsection

@section('content')
<div class="row">
<div class="row-md-4 row-md-offset-4">
	<h1> Sign Up </h1>

	
		@if(count($errors) > 0)
	<div class="alert alert-danger">
		@foreach($errors->all() as $error)
			<p>{{ $error }}</p>
		@endforeach
	</div>
		@endif
	</div>
	<form action="{{ route('user.signup') }}" method="post">
		<div class="form-group">
			<label for="name"> Name </label>
			<input type="text" id="name" name="name" pattern="[a-zA-Z\s]+" title="Use your alphabet name" required></input>
		</div>
		<div class="form-group">
			<label for="email"> E-mail </label>
			<input type="text" id="email" name="email" pattern="[A-Za-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$" title="abc@xyz.vnc" required></input>
		</div>
		<div class="form-group">
			<label for="password"> Password </label>
			<input type="password" id="password" name="password" pattern="^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W+)(?!.*\s).*$" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters without '' and space " required="required"></input>
		</div>
		<button name="signup" type="submit" class="btn btn-primary" name="signup"> Sign Up </button>
		{{ csrf_field() }}
	</form>
</div>
</div>
@endsection