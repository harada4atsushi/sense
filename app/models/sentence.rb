class Sentence < ApplicationRecord
  acts_as_taggable_on :yes_no, :feeling, :greeting, :question
end
