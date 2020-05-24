from googletrans import Translator

translator = Translator()
res = translator.translate('Сегодня хороший день для программирования ', "en")
print(res.text)
