class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception

  before_action :http_basic_authenticate if Rails.env.production?

  def http_basic_authenticate
    authenticate_or_request_with_http_basic do |name, password|
      name == 'mofmof' && password == 'mofmof-pass'
    end
  end
end
