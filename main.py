import java.util.*;

public class FakeNewsDetector {
    // List of fake news keywords (simplified)
    private static final List<String> FAKE_NEWS_KEYWORDS = Arrays.asList(
            "shocking", "clickbait", "scandal", "conspiracy", "unbelievable", "secret", "hidden truth"
    );

    public static boolean detectFakeNews(String news) {
        String lowerCaseNews = news.toLowerCase();
        
        // Check for fake news keywords
        for (String keyword : FAKE_NEWS_KEYWORDS) {
            if (lowerCaseNews.contains(keyword)) {
                return true; // Fake news detected
            }
        }
        return false; // No fake news detected
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the news article: ");
        String news = scanner.nextLine();
        scanner.close();
        
        if (detectFakeNews(news)) {
            System.out.println("Warning: This news article may contain fake news!");
        } else {
            System.out.println("This news article appears to be legitimate.");
        }
    }
}
