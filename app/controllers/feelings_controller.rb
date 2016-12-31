class FeelingsController < ApplicationController
  before_action :set_sentence, only: [:edit, :update, :destroy, :next]

  # def new
  #   @sentence = Sentence.new
  # end
  #
  def edit
  end
  #
  # def create
  #   @sentence = Sentence.new(sentence_params)
  #
  #   if @sentence.save
  #     redirect_to sentences_path, notice: 'Sentenceが作成されました'
  #   else
  #     render :new
  #   end
  # end
  #
  def update
    if @sentence.update(sentence_params)
      redirect_to next_sentence_feelings_path(@sentence), notice: 'Sentenceが更新されました'
    else
      render :edit
    end
  end

  def destroy
    @sentence.destroy
    redirect_to next_sentence_feelings_path(@sentence), notice: 'Sentenceが削除されました'
  end

  def next
    sentence = Sentence.find_untagged(@sentence, context: 'feeling')
    redirect_to edit_sentence_feelings_path(sentence)
  end

  private
    def set_sentence
      @sentence = Sentence.find(params[:sentence_id])
    end

    def sentence_params
      params.require(:sentence).permit(:body, :yes_no_list, :feeling_list, :greeting_list, :question_list)
    end
end
