/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.hittasticapp;

/**
 *
 * @author nick
 */
public class Order 
{
    private Song song;
    private int qty;
    
    public Order(Song s, int q)
    {
        song = s;
        qty = q;
    }
    
    public String toString()
    {
        return "ORDER: Song: " + song + " Quantity: " + qty;
    }
}
