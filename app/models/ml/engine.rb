class Ml::Engine

  def initialize
    @client = MessagePack::RPC::Client.new('127.0.0.1', 6000)
    @client.timeout = 20
  end

  def predict(sentences)
    @client.call(:predict, sentences).with_indifferent_access
  end
end
