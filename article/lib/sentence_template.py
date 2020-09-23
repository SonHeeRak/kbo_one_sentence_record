from article.lib import globals as g
from article.lib.sentence_generator import SentenceGenerator
from article.lib.core.log_helper import LogHelper


class DailyNewsTemplate(object):
    def __init__(self, daily_news_var):
        self.daily_news_var = daily_news_var

    def set_sentence(self):
        print('set_sentence')
        sentence_list = []
        # sentence = ''

        try:
            active_tab_list = []
            base_temp = g.MODEL_DICT['base_template']

            sg = SentenceGenerator()

            if base_temp is None:
                return sentence_list

            for bt in iter(base_temp.objects.values()):
                if bt['use'] != 'F':
                    condition_string = sg.get_result_string(sg.main_dict, bt['condition'], self.daily_news_var,
                                                            final=True)

                    if eval(condition_string):
                        if bt['template_tab'] not in active_tab_list:
                            active_tab_list.append(bt['template_tab'])
                            sg.set_variable(self.daily_news_var, bt['template_tab'])
                        print(bt['template_tab'])
                        sg.set_used_arguments_for_log(bt['sentence'], self.daily_news_var.__dict__)
                        paragraph = bt['sentence'].format(**self.daily_news_var.__dict__).strip()
                        sentences = paragraph.split('\n\n')
                        sentence_list.extend(sentences)
                        # sentence = sentences[0]

        except Exception as e:
            sentences = 'error! msg : ' + str(e) + ' \nplease generate news instead'
            sentence_list.append(sentences)
            '\n\n'.join(sentence_list)
            # sentence = sentences

            LogHelper.instance().e(str(e))

        return sentence_list
