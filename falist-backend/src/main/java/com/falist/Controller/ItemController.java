@RestController
@RequestMapping("/items")
public class ItemController {

    @Autowired
    private ItemService itemService;

    @PostMapping
    public ItemResponse create(@RequestBody ItemRequest request) {
        return itemService.create(request);
    }

    @GetMapping
    public List<ItemResponse> list() {
        return itemService.listAll();
    }
}
