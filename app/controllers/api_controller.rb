class ApiController < ApplicationController
  skip_before_action :http_basic_authenticate if Rails.env.production?
end
