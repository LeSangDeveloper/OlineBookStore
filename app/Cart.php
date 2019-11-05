<?php

namespace App;
use App\Product;

class Cart
{
	public $items = null;
	public $totalQty = 0;
	public $totalPrice = 0;

	public function __construct($oldCart)
	{
		if ($oldCart != null)
		{
			$this->items = $oldCart->items;
			$this->totalQty = $oldCart->totalQty;
			$this->totalPrice = $oldCart->totalPrice;
		}
	}

	public function add($item, $id, $quantity)
	{

		$storedItem = ['Qty' => 0, 'price' => $item->price, 'item' => $item, 'id' => $id];
		if ($this->items)
			if (array_key_exists($id, $this->items))
			{
				$storedItem = $this->items[$id];
			}
			$storedItem['Qty'] = (int)$quantity;
			$storedItem['price'] = $item->price * $quantity;
			$this->items[$id] = $storedItem;
			$this->totalQty = $this->totalQty + $quantity;
			$this->totalPrice += $storedItem['price'];
	}

	public function removeAll($id)
	{
		if($this->items[$id]['Qty'] > 0)
		{
			$this->totalQty -= $this->items[$id]['Qty'];
			$this->totalPrice -= $this->items[$id]['price'];
			unset($this->items[$id]);
		}	
	}

	public function removeOne($id)
	{
		if ($this->items[$id]['Qty'] > 0)
		{
			$product = Product::find($id);
			if ($this->items[$id]['Qty'] == 1)
			{
				
				$this->totalQty = $this->totalQty - 1;
				$this->totalPrice -= $product->price;
				unset($this->items[$id]);
				if($this->totalQty <= 0)
				{
					$this->totalPrice = 0.0;
				}
			}
			else
			{
				$this->items[$id]['Qty'] = $this->items[$id]['Qty'] - 1;
				$this->totalQty = $this->totalQty - 1;
				$this->items[$id]['price'] = $this->items[$id]['price'] - $product->price;
				$this->totalPrice = $this->totalPrice - $product->price;
			}
		}
	}
}