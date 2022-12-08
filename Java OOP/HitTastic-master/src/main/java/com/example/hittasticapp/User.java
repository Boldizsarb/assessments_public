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

public class User {
    
    private String username, password;
    private boolean adminStatus;
    private ArrayList<Order> orders = new ArrayList<>();
    
    public User(String usernameIn, String passwordIn, boolean admin)
    {
        username = usernameIn;
        password = passwordIn;
        adminStatus = admin;
    }
    
    public boolean checkCredentials(String testUsername, String testPassword)
    {
        return username.equals(testUsername) && password.equals(testPassword);
    }
    
    public String getUsername()
    {
        return username;   
    }
    
    public void setPassword(String newPassword)
    {
        password = newPassword;
    }
    
    public void setAdminStatus(boolean admin)
    {
        adminStatus = admin;
    }
    
    public boolean isAdmin()
    {
        return adminStatus;
    }
    
    public void buySong(Song s, int qty)
    {
        Order order = new Order(s, qty);
        orders.add(order);
    }
    
    public String toString()
    {
        return "Username: " + username + " Admin status: " + adminStatus;
    } 
    
    public ArrayList<Order> getOrders()
    {
        return orders;
    }
}
