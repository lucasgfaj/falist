package com.falist.Model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Data
public class User {

    @Id @GeneratedValue(strategy = GenerationType.UUID)
    private String id;

    @Column(unique = true)
    private String email;

    private String username;
    private String password; // hash BCrypt

    // Um usuário tem vários itens
    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL)
    private List<Item> itens;
}
