class Tag < ApplicationRecord
  has_many :taggings, dependent: :destroy, class_name: '::ActsAsTaggableOn::Tagging'
end
