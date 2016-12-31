class Sentence < ApplicationRecord
  acts_as_taggable_on :yes_no, :feeling, :greeting, :question

  def self.find_untagged(sentence, context: nil)
    where.not(id: sentence.id).includes(:taggings).shuffle.detect do |s|
      taggings = context.blank? ? s.taggings : s.taggings.where(context: context)
      taggings.blank?
    end
  end
end
