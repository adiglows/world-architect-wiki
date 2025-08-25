require('dotenv').config();
const { Client, GatewayIntentBits, Partials } = require('discord.js');

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
    GatewayIntentBits.GuildMessageReactions,
  ],
  partials: [Partials.Message, Partials.Channel, Partials.Reaction],
});

async function main() {
  await client.login(process.env.DISCORD_TOKEN);
  const guild = await client.guilds.fetch(process.env.GUILD_ID);
  const channel = await guild.channels.fetch(process.env.CREATIONS_CHANNEL_ID);

  const threads = await channel.threads.fetchActive();
  const featuredPosts = [];

  for (const thread of threads.threads.values()) {
    const hasFeaturedTag = thread.appliedTags.includes(process.env.FEATURED_TAG_ID);
    if (!hasFeaturedTag) continue;

    const message = await thread.fetchStarterMessage();
    const starReaction = message?.reactions.cache.find(r => r.emoji.name === '⭐');
    const starCount = starReaction?.count || 0;

    featuredPosts.push({
      title: thread.name,
      stars: starCount,
      url: message?.url || thread.url,
    });
  }

  featuredPosts.sort((a, b) => b.stars - a.stars);

  // Output Markdown
  console.log("# Featured Posts ⭐\n");
  featuredPosts.forEach(p => {
    console.log(`- [${p.title}](${p.url}) - ⭐ ${p.stars}`);
  });

  await client.destroy();
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
