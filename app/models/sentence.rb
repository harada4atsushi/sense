class Sentence < ApplicationRecord
  acts_as_taggable_on :yes_no, :feeling, :greeting, :question

  def self.find_untagged
    all.includes(:taggings).detect {|s| s.taggings.blank?}
  end
end
