<?php

namespace App\Http\Controllers;

use App\User;

use Illuminate\Http\Request;

use App\Http\Requests;

use Auth;
use Session;

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

    public function postSignin(Request $request)
    {	
    	$this->validate($request, [
    		'email' => 'email|required',
    		'password' => 'required|min:8'
    	]);

        if ($request->input('email') == "admin@lsbookstore.com")
            Session::put('admin', true);
        else
            Session::put('admin', false);

        if(Auth::attempt(['email' => $request->input('email'), 'password' => $request->input('password')]))
    	{
       		if(Session::has('oldURL'))
            {
                $oldURL = Session::get('oldURL');
                Session::forget('oldURL');
                return redirect()->to($oldURL);
            }
    	}
    	return redirect()->back();
    }

    public function postSignup(Request $request)
    {
		$this->validate($request, [
    		'email'	=>	'email|required|unique:users',
    		'password'	=>	'required|min:8'
    	]);

    	$user = new User([
    		'name'	=>	$request->input('name'),
    		'email'	=>	$request->input('email'),
    		'password' => bcrypt($request->input('password'))
    	]);

    	$user->save();

    	Auth::login($user);

        if(Session::has('oldURL'))
        {
                $oldURL = Session::get('oldURL');
                Session::forget('oldURL');
                return redirect()->to($oldURL);
        }

    	return redirect()->route('product.index');
    }

    public function getLogout()
    {
        Auth::logout();
        Session::put('admin', false);
        return redirect()->back();
    }

}
