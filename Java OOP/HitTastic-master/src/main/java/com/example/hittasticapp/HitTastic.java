/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.example.hittasticapp;

/**
 *
 * @author nick
 */

import java.util.ArrayList;

public class HitTastic 
{
    
    private ArrayList<Song> songs = new ArrayList<>();
    private ArrayList<User> users = new ArrayList<>();
    private User currentUser = null;
    
    public ArrayList<Song> findSongByTitle(String title)
    {
        ArrayList<Song> foundSongs = new ArrayList<>();
        for(Song s: songs)
        {
            if(s.getTitle().equals(title))
            {
                foundSongs.add(s);
            }
        }
        return foundSongs;
    }
    
    public ArrayList<Song> findSongByArtist(String artist)
    {
        ArrayList<Song> foundSongs = new ArrayList<>();
        for(Song s: songs)
        {
            if(s.getArtist().equals(artist))
            {
                foundSongs.add(s);
            }
        }
        return foundSongs;
    }
    
    
    public boolean buySong(long songId, int qty)
    {
        Song s = findSongById(songId);
        if (s != null && currentUser != null)
        {
            s.sell(qty);
            currentUser.buySong(s, qty);
            return true;
        }
        return false;
    }
    
    public void addSong(Song s)
    {
        songs.add(s);
    }
    
    public User login(String username, String password)
    {
        User u = findUserByUsername(username);
        if (u != null)
        {
            if (u.checkCredentials(username, password))
            {
                currentUser = u;
                return u;
            }
        }
        return null;
    }
    
    public void logout()
    {
        currentUser = null;
    }
    
    public ArrayList<User> getUsers()
    {
        return users;
    }
    
    public boolean changeUserDetails(String username, String newPassword, boolean newAdminStatus)
    {
        User u = findUserByUsername(username);
        if (u != null)
        {
            u.setPassword(newPassword);
            u.setAdminStatus(newAdminStatus);
            return true;
        }
        return false;
    }
    
    public ArrayList<Order> getCurrentUserOrders()
    {
        if(currentUser != null)
        {
            return currentUser.getOrders();
        }
        return null;
    }
    
    
    public Song findSongById(long id)
    {
        for(Song s: songs)
        {
            if(s.getId() == id)
            {
               return s;
            }
              
        }
        return null;
    }
    
    public User findUserByUsername(String username)
    {
        for(User u: users)
        {
            if(u.getUsername().equals(username))
            {
               return u;
            }
        }
        return null;
    }
}
