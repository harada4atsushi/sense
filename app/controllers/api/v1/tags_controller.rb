class Api::V1::TagsController < ApiController
  protect_from_forgery with: :null_session

  def create
    engine = Ml::Engine.new
    all_tags = Tag.all
    result = engine.predict(params[:sentences])
    tags = result[:tags].map do |tag_ids|
      tag_ids.map do |tag_id|
        tag = all_tags.detect {|t| t.id == tag_id.to_i}
        { id: tag, body: tag.name}
      end
    end
    render json: { tags: tags }
  end
end
