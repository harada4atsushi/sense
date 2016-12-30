namespace :collect do
  desc 'collect sentences from twitter'
  task :twitter, ['get_count'] => :environment do |task, args|
    get_count = (args[:get_count] || 100).to_i

    client = Twitter::Streaming::Client.new(
      consumer_key:        ENV['TWITTER_CONSUMER_KEY'],
      consumer_secret:     ENV['TWITTER_CONSUMER_SECRET'],
      access_token:        ENV['TWITTER_ACCESS_TOKEN'],
      access_token_secret: ENV['TWITTER_ACCESS_TOKEN_SECRET'],
    )

    count = 0
    client.sample do |object|
      next unless object.is_a?(Twitter::Tweet)
      next if object.user.lang != 'ja' || object.text.index('RT') || object.user_mentions?

      text = Rumoji.encode(object.text)
      puts("text: #{text}")
      Sentence.create!(body: text)

      break if count > get_count
      count = count + 1
    end
  end
end
