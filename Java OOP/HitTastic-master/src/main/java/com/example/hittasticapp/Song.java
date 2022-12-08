/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.hittasticapp;

/**
 *
 * @author nick
 */
public class Song 
{
    
    private long id;
    private String title, artist;
    private int sales;
    
    public Song(long idIn, String titleIn, String artistIn)
    {
        id = idIn;
        title = titleIn;
        artist = artistIn;
        sales = 0;
    }
    
    public void sell(int amount)
    {
        sales += amount;
    }
    
    public String toString()
    {
        return "ID: " + id + " Title: " + title + " Artist: " + artist + " Sales: " + sales;
    }  
    
    public long getId()
    {
        return id;
    }
    
    public String getTitle()
    {
        return title;
    }
    
    public String getArtist()
    {
        return artist;
    }
  
}
