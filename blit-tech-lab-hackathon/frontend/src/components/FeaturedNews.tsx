import Link from "next/link";
import { Article } from "@/utils/types";

interface NewsCardProps {
    article: Article;
}


function FeaturedNewsCard({ article }: NewsCardProps) {
    // PART 1: Display a Featured News article

    // Using the info about the article passed in as a prop, show:
    // 1. The featured article's title
    // 2. The featured article's image
    // 3. A portion of the selected article's body, truncated so that it fits nicely in the section

    // Once completing this part, you should be able to see the Featured News Article at the top of the page.

    // Hint: Some classes included in `globals.css` may help with styling.

    return (
        <>
            <span className='instruction'>Part 1: Show Featured News</span>
            <div className="featured-news-card">
                {/* TODO: Remove the span above and implement "FeaturedNewsCard" */}
            </div>
        </>
    );
}

export default FeaturedNewsCard;
