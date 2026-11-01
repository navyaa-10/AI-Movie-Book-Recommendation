import streamlit as st

st.set_page_config(
    page_title="AI Mood Recommender",
    page_icon="🎬"
)

st.title("🎬📚 AI Mood Recommender")
st.write("Find movies and books according to your mood! ❤️")

# ---------------- DATASET ----------------

recommendations = [
    # Romance
    ["The Notebook", "Romance", "Movie", "7.8/10", "Amazon Prime Video"],
    ["Titanic", "Romance", "Movie", "7.9/10", "Amazon Prime Video"],
    ["The Fault in Our Stars", "Romance", "Book", "4.4/5", "Amazon / Kindle"],
    ["The Love Hypothesis", "Romance", "Book", "4.2/5", "Amazon / Kindle"],

    # Thriller
    ["Inception", "Thriller", "Movie", "8.8/10", "Amazon Prime Video"],
    ["Gone Girl", "Thriller", "Movie", "8.1/10", "Netflix"],
    ["Verity", "Thriller", "Book", "4.4/5", "Amazon / Kindle"],
    ["The Silent Patient", "Thriller", "Book", "4.5/5", "Amazon / Kindle"],

    # Horror
    ["The Conjuring", "Horror", "Movie", "7.5/10", "Amazon Prime Video"],
    ["Insidious", "Horror", "Movie", "6.8/10", "Netflix"],
    ["Dracula", "Horror", "Book", "4.0/5", "Amazon / Kindle"],
    ["The Shining", "Horror", "Book", "4.5/5", "Amazon / Kindle"],

    # Comedy
    ["The Hangover", "Comedy", "Movie", "7.7/10", "Amazon Prime Video"],
    ["3 Idiots", "Comedy", "Movie", "8.4/10", "Netflix"],
    ["Good Omens", "Comedy", "Book", "4.2/5", "Amazon / Kindle"],
    ["Bossypants", "Comedy", "Book", "4.0/5", "Amazon / Kindle"],

    # Drama
    ["Forrest Gump", "Drama", "Movie", "8.8/10", "Netflix"],
    ["The Pursuit of Happyness", "Drama", "Movie", "8.0/10", "Amazon Prime Video"],
    ["A Thousand Splendid Suns", "Drama", "Book", "4.5/5", "Amazon / Kindle"],
    ["The Kite Runner", "Drama", "Book", "4.5/5", "Amazon / Kindle"],

    # Mystery
    ["Knives Out", "Mystery", "Movie", "7.9/10", "Netflix"],
    ["Sherlock Holmes", "Mystery", "Movie", "7.6/10", "Amazon Prime Video"],
    ["The Inheritance Games", "Mystery", "Book", "4.3/5", "Amazon / Kindle"],
    ["One of Us Is Lying", "Mystery", "Book", "4.1/5", "Amazon / Kindle"],

    # Sci-Fi
    ["Interstellar", "Sci-Fi", "Movie", "8.7/10", "JioHotstar"],
    ["The Matrix", "Sci-Fi", "Movie", "8.7/10", "Amazon Prime Video"],
    ["Dune", "Sci-Fi", "Book", "4.4/5", "Amazon / Kindle"],
    ["The Martian", "Sci-Fi", "Book", "4.4/5", "Amazon / Kindle"],

    # Fantasy
    ["Harry Potter", "Fantasy", "Movie", "8.1/10", "JioHotstar"],
    ["The Hobbit", "Fantasy", "Movie", "7.8/10", "Amazon Prime Video"],
    ["Harry Potter", "Fantasy", "Book", "4.8/5", "Amazon / Kindle"],
    ["The Hobbit", "Fantasy", "Book", "4.6/5", "Amazon / Kindle"],

    # Action
    ["Avengers Endgame", "Action", "Movie", "8.4/10", "Disney+"],
    ["John Wick", "Action", "Movie", "7.4/10", "Amazon Prime Video"],
    ["The Hunger Games", "Action", "Book", "4.3/5", "Amazon / Kindle"],
    ["Divergent", "Action", "Book", "4.2/5", "Amazon / Kindle"],

    # Adventure
    ["Jumanji", "Adventure", "Movie", "6.9/10", "Netflix"],
    ["Jurassic Park", "Adventure", "Movie", "8.2/10", "Amazon Prime Video"],
    ["The Alchemist", "Adventure", "Book", "4.2/5", "Amazon / Kindle"],
    ["Around the World in 80 Days", "Adventure", "Book", "4.0/5", "Amazon / Kindle"],

    # Feel-Good
    ["The Intern", "Feel-Good", "Movie", "7.1/10", "Netflix"],
    ["Paddington", "Feel-Good", "Movie", "7.2/10", "Amazon Prime Video"],
    ["Wonder", "Feel-Good", "Book", "4.5/5", "Amazon / Kindle"],
    ["The Little Prince", "Feel-Good", "Book", "4.4/5", "Amazon / Kindle"],

    # Sad
    ["Me Before You", "Sad", "Movie", "7.4/10", "Amazon Prime Video"],
    ["A Star Is Born", "Sad", "Movie", "7.6/10", "JioHotstar"],
    ["It Ends with Us", "Sad", "Book", "4.3/5", "Amazon / Kindle"],
    ["The Fault in Our Stars", "Sad", "Book", "4.4/5", "Amazon / Kindle"]
]

# ---------------- MOODS ----------------

moods = [
    "Romance",
    "Thriller",
    "Horror",
    "Comedy",
    "Drama",
    "Mystery",
    "Sci-Fi",
    "Fantasy",
    "Action",
    "Adventure",
    "Feel-Good",
    "Sad"
]

# ---------------- USER INPUT ----------------

selected_mood = st.selectbox(
    "🎭 Select your mood:",
    moods
)

selected_type = st.radio(
    "What do you want?",
    ["🎬 Movie", "📚 Book"]
)

# Convert Movie/Book selection
if selected_type == "🎬 Movie":
    content_type = "Movie"
else:
    content_type = "Book"

# ---------------- RECOMMENDATION ENGINE ----------------

results = [
    item for item in recommendations
    if item[1] == selected_mood and item[2] == content_type
]

# ---------------- DISPLAY ----------------

st.write("---")
st.subheader("✨ Recommended for You")

if results:

    for item in results:

        title = item[0]
        mood = item[1]
        content = item[2]
        rating = item[3]
        platform = item[4]

        st.markdown(f"## {'🎬' if content == 'Movie' else '📚'} {title}")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"⭐ **Rating:** {rating}")

        with col2:
            st.write(f"📺 **Available on:** {platform}")

        st.write(f"🎭 **Mood:** {mood}")

        st.divider()

else:
    st.warning("No recommendation found for this selection.")

# ---------------- FOOTER ----------------

st.info("💡 Recommendations are generated according to your selected mood and content type.")
