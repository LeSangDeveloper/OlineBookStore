<?php

use Illuminate\Database\Seeder;
use App\Product;

class ProductTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        //
        $product = new Product([
        	'title' => 'Harry Potter',
        	'imagePath' => '...',
        	'description' => 'A best fiction novel of J.K Rowling',
        	'inStock' => 10,
        	'price' => 25.12,
        	'author' => 'J.K Rowling'
        ]);
        $product->save();

        $product = new Product([
            'imagePath' => 'public/src/images/th1.jpg',
            'title' => 'Introduction to algorithms',
            'description' => 'Best for fresher IT student',
            'price' => 20,
            'inStock' => 20,
            'author' => 'Thomas H. Cormen'
        ]);
        $product->save();

        $product = new Product([
            'imagePath' => 'public/src/images/th2.jpg',
            'title' => 'Linux Bible',
            'description' => 'Beginning for Linux-er',
            'price' => 25,
            'inStock' => 15,
            'author' => 'Christopher Negus'
        ]);
        $product->save();

        $product = new Product([
            'imagePath' => 'public/src/images/th3.jpg',
            'title' => 'Operating System Principle',
            'description' => 'for CS student',
            'price' => 30,
            'inStock' => 15,
            'author' => 'Alan C. Shaw'
        ]);
        $product->save();

        $product = new Product([
            'imagePath' => 'public/src/images/th4.jpg',
            'title' => 'Learn C the Hard Way',
            'description' => 'Best of the C Programming Books',
            'price' => 15,
            'inStock' => 15,
            'author' => 'Zed Shaw'
        ]);
        $product->save();

        $product = new Product([
            'imagePath' => 'public/src/images/th5.jpg',
            'title' => 'The art of Computer Programming',
            'description' => 'Best of the Programming book',
            'price' => 12,
            'inStock' => 15,
            'author' => 'Donald Knuth' 
        ]);
        $product->save();
    }
}
