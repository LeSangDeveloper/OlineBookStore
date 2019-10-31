<?php

namespace App;

class Cart
{
	public $items = null;
	public $totalQty = 0;
	public $totalPrice = 0;

	public function __construct($oldCart)
	{
		if ($oldCart != n)
		{
			$this->items = $oldCart->items;
			$this->totalQty = $oldCart->totalQty;
			$this->totalPrice = $oldCart->totalPrice;
		}
	}

	public function add($item, $id)
	{
		$storedItem = ['Qty' => 0, 'price' => $item->price, 'item' => $item];
		if ($this->items != null)
				if(array_key_exists($id, $this->items))
				{
					$storedItem['item']  = $this->items[$id];
				}
				$storedItem['Qty']++;
				$this->item[$id] = $storedItem['item'];
				$this->totalQty += $storedItem['Qty'];
				$this->totalPrice += $totalPrice['price'];

	}
}