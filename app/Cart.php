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
		$storedItem = ['id' => 0, 'Qty' => 0, 'price' => 0, 'item' => $item];
		if ($this->items)
				if(array_key_exists($id, $this->items))
				{
					$storedItem  = $this->items[$id];
				}
				$storedItem['Qty']++;
				$storedItem['id'] = $id;
				$storedItem['price'] = $item->price;

				$this->items[$id] = $storedItem;

				$this->totalQty += 1;
				$this->totalPrice += $storedItem['price'];

	}

	public function removeAll($id)
	{
		$this->totalQty -= $this->items[$id]['Qty'];
		$this->totalPrice -= $this->items[$id]['price'] * $this->items[$id]['Qty'];
		unset($this->items[$id]);
	}

	public function removeOne($id)
	{
		if ($this->items[$id]['Qty'] == 1)
		{
			$this->totalQty -= 1;
			$this->totalPrice -= $this->items[$id]['price'];
			unset($this->items[$id]);
		}
		else
		{
			$this->totalQty -= 1;
			$this->totalPrice -= $this->items[$id]['price'];
		}
	}
}