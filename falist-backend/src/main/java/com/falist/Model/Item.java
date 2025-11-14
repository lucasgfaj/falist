@Entity
public class Item {

    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String title;

    @Enumerated(EnumType.STRING)
    private TypeItem type; // FILME, ANIME, SERIE, MANHWA, LIVRO

    @Enumerated(EnumType.STRING)
    private StatusItem status; // ASSISTINDO, FINALIZADO, PAUSADO

    private String imageUrl;
    private String link;

    @ManyToOne
    private Category category;

    @ManyToOne
    private User user;
}
