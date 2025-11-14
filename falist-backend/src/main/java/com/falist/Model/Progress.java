@Entity
public class Progress {

    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Integer currentEpisode;
    private Integer currentChapter;

    private LocalDateTime updatedOn = LocalDateTime.now();

    @OneToOne
    private Item item;
}
