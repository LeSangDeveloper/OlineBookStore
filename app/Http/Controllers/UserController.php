<?php

namespace App\Http\Controllers;

use App\User;

use Illuminate\Http\Request;

use App\Http\Requests;

class UserController extends Controller
{
    //
    public function getSignup()
    {
    	return view('user.signup');
    }

    public function getSignin()
    {
    	return view('user.signin');
    }

    public function postSignin()
    {

    }

    public function postSignup()
    {
    	
    }

}
