class SentencesController < ApplicationController
  before_action :set_sentence, only: [:show, :edit, :update, :destroy]

  # GET /sentences
  def index
    @sentences = Sentence.all
  end

  # GET /sentences/1
  def show
  end

  # GET /sentences/new
  def new
    @sentence = Sentence.new
  end

  # GET /sentences/1/edit
  def edit
  end

  # POST /sentences
  def create
    @sentence = Sentence.new(sentence_params)

    if @sentence.save
      redirect_to sentences_path, notice: 'Sentenceが作成されました'
    else
      render :new
    end
  end

  # PATCH/PUT /sentences/1
  def update
    if @sentence.update(sentence_params)
      redirect_to sentences_path, notice: 'Sentenceが更新されました'
    else
      render :edit
    end
  end

  # DELETE /sentences/1
  def destroy
    @sentence.destroy
    redirect_to sentences_url, notice: 'Sentenceが削除されました'
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_sentence
      @sentence = Sentence.find(params[:id])
    end

    # Only allow a trusted parameter "white list" through.
    def sentence_params
      params.require(:sentence).permit(:body)
    end
end
