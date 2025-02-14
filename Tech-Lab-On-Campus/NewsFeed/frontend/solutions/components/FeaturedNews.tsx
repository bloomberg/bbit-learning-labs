import Link from "next/link";
import { Article } from "@/utils/types";

interface NewsCardProps {
    article: Article;
}


function FeaturedNewsCard({ article }: NewsCardProps) {
    return (
        <div className="featured-news-card">
            <div className="featured-news-img-div">
                <img
                    src={article.image_url}
                    alt={article.title}
                    className="featured-news-img"
                />
            </div>
            <div className="featured-news-info">
                <h2 className="featured-story-title">{article.title}</h2>
                <p className="featured-story-summary">{article.body}</p>
                {article.author && <span className="featured-story-author">By {article.author}</span>}
                {article.url &&
                    <span className="featured-story-author" >
                        Via <Link className="origin-link" href={article.url} target="_blank">{article.url}</Link>
                    </span>
                }
            </div>
        </div>
    );
}

export default FeaturedNewsCard;
