<?php

namespace App;

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

	public function add($item, $id)
	{
		$storedItem = ['Qty' => 0, 'price' => $item->price, 'item' => $item];
		if ($this->items)
				if(array_key_exists($id, $this->items))
				{
					$storedItem  = $this->items[$id];
				}
				$storedItem['Qty']++;
				$this->items[$id] = $storedItem;
				$this->totalQty += 1;
				$this->totalPrice += $storedItem['price'];

	}
}