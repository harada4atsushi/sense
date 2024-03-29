source 'https://rubygems.org'
ruby '2.3.3'

# Bundle edge Rails instead: gem 'rails', github: 'rails/rails'
gem 'rails', '~> 5.0.0'

# select DB for local server
gem 'mysql2'
# gem 'sqlite3', :group => :development
# gem 'pg'

# Use SCSS for stylesheets
gem 'sass'
gem 'sass-rails', '~> 5.0'
gem 'font-awesome-rails'

# easy to write a form
gem 'bootstrap-sass'
gem 'bootstrap_form'
#gem 'simple_form' #代替案

# Use Uglifier as compressor for JavaScript assets
gem 'uglifier', '>= 1.3.0'
# Use CoffeeScript for .coffee assets and views
gem 'coffee-rails'
# See https://github.com/sstephenson/execjs#readme for more supported runtimes
gem 'therubyracer', platforms: :ruby

# Use jquery as the JavaScript library
gem 'jquery-rails'
# Turbolinks makes following links in your web application faster. Read more: https://github.com/rails/turbolinks
gem 'turbolinks'
# Build JSON APIs with ease. Read more: https://github.com/rails/jbuilder
gem 'jbuilder'
# bundle exec rake doc:rails generates the API under doc/api.
gem 'sdoc'

# pagination
gem 'kaminari'

# Use ActiveModel has_secure_password
gem 'bcrypt'

# login
gem 'devise'
gem 'devise-bootstrap-views'
gem 'devise-i18n'
gem 'devise-i18n-views'

# admin pages
gem 'rails_admin'

# enum with i18n
gem 'enum_help'

# Use Unicorn as the app server
gem 'unicorn'

# Use Capistrano for deployment
# gem 'capistrano-rails', group: :development

# Seed Data Management
gem 'seed-fu'

gem 'puma', group: :development

gem 'config'
gem 'twitter'
gem 'dotenv-rails'
gem 'rumoji'
gem 'slim-rails'
gem 'acts-as-taggable-on', '~> 4.0'
gem 'bootstrap-tagsinput-rails'
gem 'msgpack-rpc', '~> 0.5.4'

group :development, :test do

  # Call 'byebug' anywhere in the code to stop execution and get a debugger console
  gem 'byebug'
  gem 'rubocop'

  # N+1問題検出
  gem 'bullet'

  # Access an IRB console on exception pages or by using <%= console %> in views
  # 現時点では、better_errorsの方が使いやすい
#  gem 'web-console', '~> 2.0'
  # Debug
  gem 'better_errors'
  gem 'binding_of_caller'

  # Spring speeds up development by keeping your application running in the background. Read more: https://github.com/rails/spring
  gem 'spring'

  gem 'pry-byebug'
  gem 'pry-rails'
  gem 'pry-doc'
  gem 'pry-stack_explorer'

  # rspec
  gem 'rspec-rails', '~> 3.5.0'
  gem 'factory_girl_rails'
  gem 'guard'
  gem 'guard-rspec'
  gem 'capybara'
  gem 'selenium-webdriver'

  # dummy data
  gem 'faker'

  gem 'database_cleaner'
  gem 'letter_opener'
end

group :production, :staging do
  # Heroku用DB
  #gem 'pg'
  # ログ保存先変更、静的アセット Heroku 向けに調整
  gem 'rails_12factor'
end
