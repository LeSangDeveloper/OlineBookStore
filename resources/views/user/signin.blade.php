@extends('layouts.master')

@section('title')
LS BookStore
@endsection

@section('content')
<div class="row">
<div class="row-md-4 row-md-offset-4">
	<h1> Sign In </h1>

	
		@if(count($errors) > 0)
	<div class="alert alert-danger">
		@foreach($errors->all() as $error)
			<p>{{ $error }}</p>
		@endforeach
	</div>
		@endif
	</div>
	<form action="{{ route('user.signin') }}" method="post">
		<div class="form-group">
			<label for="email"> E-mail </label>
			<input type="text" id="email" name="email" pattern="[A-Za-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$" title="abc@xyz.vnc" required></input>
		</div>
		<div class="form-group">
			<label for="password"> Password </label>
			<input type="password" id="password" name="password" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!`~@#$%^&*()\])(?!.*[\s]).{6,20}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters without '' and ' and space" required></input>
		</div>
		<button type="submit" class="btn btn-primary" name="signin"> Sign In </button>
		{{ csrf_field() }}
	</form>
	<p>If you don't have account.</p><a href="{{ route('user.signup') }}">Sign Up instead.</a>
</div>
</div>
@endsection