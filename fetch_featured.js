require('dotenv').config();
const fs = require("fs");
const { Client, GatewayIntentBits, Partials, ActivityType } = require('discord.js');

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
    GatewayIntentBits.GuildMessageReactions,
  ],
  partials: [Partials.Message, Partials.Channel, Partials.Reaction],
});

client.once('ready', async () => {
  console.log(`Logged in as ${client.user.tag}!`);

  try {
    // Small delay so Discord is ready
    await new Promise(resolve => setTimeout(resolve, 2000));

    // Set bot presence
    client.user.setPresence({
      activities: [{
        name: process.env.BOT_STATUS_MESSAGE || 'Watching for featured posts',
        type: ActivityType.Watching
      }],
      status: 'online'
    });

    console.log('Bot status set successfully');

    // Fetch and write featured posts
    await checkFeaturedPosts();

    // Exit after writing (important for GitHub Actions)
    process.exit(0);
  } catch (error) {
    console.error('Error in ready event:', error);
    process.exit(1);
  }
});

async function checkFeaturedPosts() {
  try {
    const guild = client.guilds.cache.get(process.env.GUILD_ID);
    if (!guild) throw new Error('Guild not found');

    const channel = guild.channels.cache.get(process.env.CREATIONS_CHANNEL_ID);
    if (!channel || !channel.isThreadOnly()) throw new Error('Invalid forum channel');

    const threads = await channel.threads.fetchActive();
    const featuredPosts = [];

    for (const thread of threads.threads.values()) {
      const hasFeaturedTag = thread.appliedTags.includes(process.env.FEATURED_TAG_ID);

      if (hasFeaturedTag) {
        const message = await thread.fetchStarterMessage();
        if (!message) continue;

        const starReaction = message.reactions.cache.find(r => r.emoji.name === '⭐');
        const starCount = starReaction?.count || 0;

        // Get preview of message content
        let preview = message.content?.trim() || '';
        if (preview.length > 200) preview = preview.slice(0, 200) + '...';

        // Get first image attachment (if any)
        let imageMarkdown = '';
        if (message.attachments.size > 0) {
          const img = message.attachments.find(att => att.contentType?.startsWith('image/'));
          if (img) {
            imageMarkdown = `\n\n![image](${img.url})`;
          }
        }

        featuredPosts.push({
          title: thread.name,
          url: message.url || thread.url,
          stars: starCount,
          preview,
          imageMarkdown,
        });
      }
    }

    // Sort posts by star count
    featuredPosts.sort((a, b) => b.stars - a.stars);

    // Ranking emojis for top 3
    const rankEmojis = ["🥇", "🥈", "🥉"];

    // Build markdown output
    let output = "# Featured Posts ⭐\n\n";
    if (featuredPosts.length === 0) {
      output += "_No featured posts found._\n";
    } else {
      featuredPosts.forEach((p, i) => {
        let titleLine = `## ${p.title} (⭐ ${p.stars})`;
        if (i < 3) {
          titleLine = `## ${rankEmojis[i]} ${p.title} (⭐ ${p.stars})`;
        }

        output += `${titleLine}\n`;
        output += `[View Post](${p.url})\n\n`;
        if (p.preview) output += `${p.preview}\n`;
        if (p.imageMarkdown) output += `${p.imageMarkdown}\n`;
        output += `\n---\n\n`;
      });
    }

    // Save to markdown file
    fs.writeFileSync("featured_posts.md", output.trim() + "\n");
    console.log("✅ featured_posts.md updated!");
  } catch (error) {
    console.error('Error checking featured posts:', error);
  }
}

client.login(process.env.DISCORD_TOKEN);
