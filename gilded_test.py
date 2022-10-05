from glided import GildedRose,Item
import copy

def test_dec_x2(): #dec of quality is twice as fast when the sellin days are over
    store = GildedRose([Item("Orb of deception",0,0)])
    if store.items[0].quality > 1:# 1 and below doesn't dec by 2 rather turns to 0
        store_copy = copy.deepcopy(store)
        store.update_quality()
        print(store.items)
        assert store_copy.items[0].quality - 2 == store.items[0].quality, "didnt degrade quality twice as fast"
    else:
        store.update_quality()
        print(store.items)
        assert store.items[0].quality == 0

def test_negative_quality():
    store = GildedRose([Item("Dull Sword",0,0)]) #if quality <0 from creation then it won't work
    store.update_quality()
    print(store.items)
    assert store.items[0].quality >= 0, "quality of an item came out negative"

def test_Brie_aging():
    store = GildedRose([Item("Aged Brie",0,50)])
    if store.items[0].quality < 50:
        store_copy = copy.deepcopy(store)
        store.update_quality()
        assert store.items[0].quality > store_copy.items[0].quality, "didn't aged well"
        print(store.items)
    else:
        store.update_quality()
        print(store.items)
        assert store.items[0].quality == 50

def test_over_50(): # there is no statment stating the base price cannot be above 50. for example creating dull sword costing 70.
    store = GildedRose([Item("Aged Brie",2,50),Item("Backstage passes to a TAFKAL80ETC concert",2,50)])
    store.update_quality()
    print(store.items)
    assert store.items[0].quality and store.items[1].quality == 50

def test_Sulfurus():
    store = GildedRose([Item("Sulfuras, Hand of Ragnaros",0,80)])
    store.update_quality()
    print(store.items)
    assert store.items[0].quality == 80

def test_backstage_inc():
    store = GildedRose([Item("Backstage passes to a TAFKAL80ETC concert",11,10)])
    while store.items[0].sell_in > 10:
        store_copy = copy.deepcopy(store)
        store.update_quality()
        print(store.items)
        assert store.items[0].quality - 1 == store_copy.items[0].quality
    while 5 < store.items[0].sell_in < 11:
        store_copy = copy.deepcopy(store)
        store.update_quality()
        print(store.items)
        assert store.items[0].quality - 2 == store_copy.items[0].quality
    while 0 < store.items[0].sell_in < 6:
        store_copy = copy.deepcopy(store)
        store.update_quality()
        print(store.items)
        assert store.items[0].quality - 3 == store_copy.items[0].quality          
    store.update_quality()
    print(store.items)
    assert store.items[0].quality == 0
    

def test_conjured():
    store = GildedRose([Item("Conjured",1,7)])
    while store.items[0].sell_in > 0 and store.items[0].quality > 1:
        store_copy = copy.deepcopy(store)
        store.update_quality()
        print(store.items)
        assert store_copy.items[0].quality -2 == store.items[0].quality 
    while store.items[0].quality > 3: 
        store_copy = copy.deepcopy(store)
        store.update_quality()
        print(store.items)
        assert store_copy.items[0].quality - 4 == store.items[0].quality
    while store.items[0].quality >= 0 and store.items[0].sell_in > -2:
        store_copy = copy.deepcopy(store)
        store.update_quality()
        print(store.items)
        assert store.items[0].quality >= 0

