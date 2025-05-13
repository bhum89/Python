import random
import time


def login(username, password):
    print(f"Logging in as {username}...")
    time.sleep(1)
    print("Login successful!\n")


def generate_fake_posts(hashtag, count=5):
    fake_users = ["@naturelover", "@chef_mom", "@dev_coder", "@art_queen", "@travel_guru"]
    posts = []
    for _ in range(count):
        user = random.choice(fake_users)
        post_id = random.randint(1000, 9999)
        posts.append({"user": user, "post_id": post_id})
    return posts


def like_and_follow(posts):
    liked_users = []
    followed_users = []

    for post in posts:
        print(f"\n📸 Post ID: {post['post_id']} by {post['user']}")

        like = input("→ Like this post? (y/n): ").lower()
        if like == 'y':
            print(f"✔️ Liked post {post['post_id']}")
            liked_users.append(post['user'])
        else:
            print("❌ Skipped liking.")

        follow = input("→ Follow this user? (y/n): ").lower()
        if follow == 'y':
            print(f"✔️ Followed {post['user']}")
            followed_users.append(post['user'])
        else:
            print("❌ Skipped following.")

        print("-" * 40)
        time.sleep(1)

   
    print("\n✅ Action Summary:")
    print(f"👉 Total posts viewed: {len(posts)}")
    print(f"❤️ Posts liked: {len(liked_users)}")
    print(f"➕ Users followed: {len(followed_users)}")
    if followed_users:
        print(f"📝 Followed Users List: {', '.join(followed_users)}")
    else:
        print("📝 Followed Users List: None")


def main():
    print("🧠 Instagram Automation Simulator (Offline)")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    login(username, password)

    hashtag = input("\n🔍 Enter a hashtag to search: #")
    print(f"\nFetching posts under #{hashtag}...\n")
    time.sleep(1)

    posts = generate_fake_posts(hashtag)
    like_and_follow(posts)

    print("\n📴 Logged out. Thank you for using the simulator!")


if __name__ == "__main__":
    main()
