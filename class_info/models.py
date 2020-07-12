from django.db import models


sem = (
    ("通年", "通年"),
    ("春夏", "春夏"),
    ("春クオーター", "春クオーター"),
    ("夏クォーター", "夏クォーター"),
    ("秋冬", "秋冬"),
    ("秋クォータ", "秋クォータ"),
    ("冬クォーター", "冬クォーター")
)
star = (
    ("★ 5", "★ 5"),
    ("★ 4", "★ 4"),
    ("★ 3", "★ 3"),
    ("★ 2", "★ 2"),
    ("★ 1", "★ 1")
)
tf = (
    ("有", "有"),
    ("無", "無")
)
ne = (
    ("要", "要"),
    ("不", "不")
)
atte = (
    ("点呼", "点呼"),
    ("課題提出", "課題提出"),
    ("出席カード", "出席カード"),
    ("確認なし", "確認なし")
)
assi = (
    ("重", "重"),
    ("普", "普"),
    ("軽", "軽")
)
ok = (
    ("可", "可"),
    ("不", "不")
)


class SK(models.Model):

    clas = models.CharField(max_length = 25, verbose_name = "科目")
    semes = models.TextField(choices = sem, null = True, verbose_name = "学期")
    prof = models.CharField(max_length = 25, default = "", verbose_name = "先生")
    ease = models.TextField(choices = star, null = True, verbose_name = "楽単度")
    aplus = models.TextField(choices = star, null = True, verbose_name = "評価A以上")
    fulfil = models.TextField(choices = star, null = True, verbose_name = "内容")
    test = models.TextField(choices = tf, null = True, verbose_name = "小テスト")
    exam = models.TextField(choices = tf, null = True, verbose_name = "期末テスト")
    cheat = models.TextField(choices = ok, null = True, verbose_name = "試験レジュメ持ち込み")
    attend = models.TextField(choices = atte, null = True, verbose_name = "出席")
    presen = models.TextField(choices = tf, null = True, verbose_name = "プレゼン")
    assig = models.TextField(choices = assi, null = True, verbose_name = "課題重さ")
    comme = models.TextField(max_length = 50, null = True, verbose_name = "")
    contributor = models.TextField(max_length = 50, null = True, verbose_name = "投稿者")
    like = models.IntegerField(null = True, default = 0)
    date = models.TextField(null = True)

    def __str__(self):
        return self.clas


class SY(models.Model):

    clas = models.CharField(max_length = 25, verbose_name = "科目")
    semes = models.TextField(choices = sem, null = True, verbose_name = "学期")
    prof = models.CharField(max_length = 25, default = "", verbose_name = "先生")
    ease = models.TextField(choices = star, null = True, verbose_name = "楽単度")
    aplus = models.TextField(choices = star, null = True, verbose_name = "評価A以上")
    fulfil = models.TextField(choices = star, null = True, verbose_name = "内容")
    test = models.TextField(choices = tf, null = True, verbose_name = "小テスト")
    exam = models.TextField(choices = tf, null = True, verbose_name = "期末テスト")
    cheat = models.TextField(choices = ok, null = True, verbose_name = "試験レジュメ持ち込み")
    attend = models.TextField(choices = atte, null = True, verbose_name = "出席")
    presen = models.TextField(choices = tf, null = True, verbose_name = "プレゼン")
    assig = models.TextField(choices = assi, null = True, verbose_name = "課題重さ")
    comme = models.TextField(max_length = 50, null = True, verbose_name = "")
    contributor = models.TextField(max_length = 50, null=True, verbose_name="投稿者")
    like = models.IntegerField(null = True, default = 0)
    date = models.TextField(null = True)

    def __str__(self):
        return self.clas


class HO(models.Model):

    clas = models.CharField(max_length = 25, verbose_name = "科目")
    semes = models.TextField(choices = sem, null = True, verbose_name = "学期")
    prof = models.CharField(max_length = 25, default = "", verbose_name = "先生")
    ease = models.TextField(choices = star, null = True, verbose_name = "楽単度")
    aplus = models.TextField(choices = star, null = True, verbose_name = "評価A以上")
    fulfil = models.TextField(choices = star, null = True, verbose_name = "内容")
    test = models.TextField(choices = tf, null = True, verbose_name = "小テスト")
    exam = models.TextField(choices = tf, null = True, verbose_name = "期末テスト")
    cheat = models.TextField(choices = ok, null = True, verbose_name = "試験レジュメ持ち込み")
    attend = models.TextField(choices = atte, null = True, verbose_name = "出席")
    presen = models.TextField(choices = tf, null = True, verbose_name = "プレゼン")
    assig = models.TextField(choices = assi, null = True, verbose_name = "課題重さ")
    comme = models.TextField(max_length = 50, null = True, verbose_name = "")
    contributor = models.TextField(max_length = 50, null = True, verbose_name = "投稿者")
    like = models.IntegerField(null = True, default = 0)
    date = models.TextField(null = True)

    def __str__(self):
        return self.clas


class SG(models.Model):

    clas = models.CharField(max_length = 25, verbose_name = "科目")
    semes = models.TextField(choices = sem, null = True, verbose_name = "学期")
    prof = models.CharField(max_length = 25, default = "", verbose_name = "先生")
    ease = models.TextField(choices = star, null = True, verbose_name = "楽単度")
    aplus = models.TextField(choices = star, null = True, verbose_name = "評価A以上")
    fulfil = models.TextField(choices = star, null = True, verbose_name = "内容")
    test = models.TextField(choices = tf, null = True, verbose_name = "小テスト")
    exam = models.TextField(choices = tf, null = True, verbose_name = "期末テスト")
    cheat = models.TextField(choices = ok, null = True, verbose_name = "試験レジュメ持ち込み")
    attend = models.TextField(choices = atte, null = True, verbose_name = "出席")
    presen = models.TextField(choices = tf, null = True, verbose_name = "プレゼン")
    assig = models.TextField(choices = assi, null = True, verbose_name = "課題重さ")
    comme = models.TextField(max_length = 50, null = True, verbose_name = "")
    contributor = models.TextField(max_length = 50, null = True, verbose_name = "投稿者")
    like = models.IntegerField(null = True, default = 0)
    date = models.TextField(null = True)

    def __str__(self):
        return self.clas


class KY(models.Model):

    clas = models.CharField(max_length = 25, verbose_name = "科目")
    semes = models.TextField(choices = sem, null = True, verbose_name = "学期")
    prof = models.CharField(max_length = 25, default = "", verbose_name = "先生")
    ease = models.TextField(choices = star, null = True, verbose_name = "楽単度")
    aplus = models.TextField(choices = star, null = True, verbose_name = "評価A以上")
    fulfil = models.TextField(choices = star, null = True, verbose_name = "内容")
    test = models.TextField(choices = tf, null = True, verbose_name = "小テスト")
    exam = models.TextField(choices = tf, null = True, verbose_name = "期末テスト")
    cheat = models.TextField(choices = ok, null = True, verbose_name = "試験レジュメ持ち込み")
    attend = models.TextField(choices = atte, null = True, verbose_name = "出席")
    presen = models.TextField(choices = tf, null = True, verbose_name = "プレゼン")
    assig = models.TextField(choices = assi, null = True, verbose_name = "課題重さ")
    comme = models.TextField(max_length = 50, null = True, verbose_name = "")
    contributor = models.TextField(max_length = 50, null = True, verbose_name = "投稿者")
    like = models.IntegerField(null = True, default = 0)
    date = models.TextField(null = True)

    def __str__(self):
        return self.clas


class BU(models.Model):

    clas = models.CharField(max_length = 25, verbose_name = "科目")
    semes = models.TextField(choices = sem, null = True, verbose_name = "学期")
    prof = models.CharField(max_length = 25, default = "", verbose_name = "先生")
    ease = models.TextField(choices = star, null = True, verbose_name = "楽単度")
    aplus = models.TextField(choices = star, null = True, verbose_name = "評価A以上")
    fulfil = models.TextField(choices = star, null = True, verbose_name = "内容")
    test = models.TextField(choices = tf, null = True, verbose_name = "小テスト")
    exam = models.TextField(choices = tf, null = True, verbose_name = "期末テスト")
    cheat = models.TextField(choices = ok, null = True, verbose_name = "試験レジュメ持ち込み")
    attend = models.TextField(choices = atte, null = True, verbose_name = "出席")
    presen = models.TextField(choices = tf, null = True, verbose_name = "プレゼン")
    assig = models.TextField(choices = assi, null = True, verbose_name = "課題重さ")
    comme = models.TextField(max_length = 50, null = True, verbose_name = "")
    contributor = models.TextField(max_length = 50, null = True, verbose_name = "投稿者")
    like = models.IntegerField(null = True, default = 0)
    date = models.TextField(null = True)

    def __str__(self):
        return self.clas


class BK(models.Model):

    clas = models.CharField(max_length = 25, verbose_name = "科目")
    semes = models.TextField(choices = sem, null = True, verbose_name = "学期")
    prof = models.CharField(max_length = 25, default = "", verbose_name = "先生")
    ease = models.TextField(choices = star, null = True, verbose_name = "楽単度")
    aplus = models.TextField(choices = star, null = True, verbose_name = "評価A以上")
    fulfil = models.TextField(choices = star, null = True, verbose_name = "内容")
    test = models.TextField(choices = tf, null = True, verbose_name = "小テスト")
    exam = models.TextField(choices = tf, null = True, verbose_name = "期末テスト")
    cheat = models.TextField(choices = ok, null = True, verbose_name = "試験レジュメ持ち込み")
    attend = models.TextField(choices = atte, null = True, verbose_name = "出席")
    presen = models.TextField(choices = tf, null = True, verbose_name = "プレゼン")
    assig = models.TextField(choices = assi, null = True, verbose_name = "課題重さ")
    comme = models.TextField(max_length = 50, null = True, verbose_name = "")
    contributor = models.TextField(max_length = 50, null = True, verbose_name = "投稿者")
    like = models.IntegerField(null = True, default = 0)
    date = models.TextField(null = True)

    def __str__(self):
        return self.clas


class KI(models.Model):

    clas = models.CharField(max_length = 25, verbose_name = "科目")
    semes = models.TextField(choices = sem, null = True, verbose_name = "学期")
    prof = models.CharField(max_length = 25, default = "", verbose_name = "先生")
    ease = models.TextField(choices = star, null = True, verbose_name = "楽単度")
    aplus = models.TextField(choices = star, null = True, verbose_name = "評価A以上")
    fulfil = models.TextField(choices = star, null = True, verbose_name = "内容")
    test = models.TextField(choices = tf, null = True, verbose_name = "小テスト")
    exam = models.TextField(choices = tf, null = True, verbose_name = "期末テスト")
    cheat = models.TextField(choices = ok, null = True, verbose_name = "試験レジュメ持ち込み")
    attend = models.TextField(choices = atte, null = True, verbose_name = "出席")
    presen = models.TextField(choices = tf, null = True, verbose_name = "プレゼン")
    assig = models.TextField(choices = assi, null = True, verbose_name = "課題重さ")
    comme = models.TextField(max_length = 50, null = True, verbose_name = "")
    contributor = models.TextField(max_length = 50, null = True, verbose_name = "投稿者")
    like = models.IntegerField(null = True, default = 0)
    date = models.TextField(null = True)

    def __str__(self):
        return self.clas


class SO(models.Model):

    clas = models.CharField(max_length = 25, verbose_name = "科目")
    semes = models.TextField(choices = sem, null = True, verbose_name = "学期")
    prof = models.CharField(max_length = 25, default = "", verbose_name = "先生")
    ease = models.TextField(choices = star, null = True, verbose_name = "楽単度")
    aplus = models.TextField(choices = star, null = True, verbose_name = "評価A以上")
    fulfil = models.TextField(choices = star, null = True, verbose_name = "内容")
    test = models.TextField(choices = tf, null = True, verbose_name = "小テスト")
    exam = models.TextField(choices = tf, null = True, verbose_name = "期末テスト")
    cheat = models.TextField(choices = ok, null = True, verbose_name = "試験レジュメ持ち込み")
    attend = models.TextField(choices = atte, null = True, verbose_name = "出席")
    presen = models.TextField(choices = tf, null = True, verbose_name = "プレゼン")
    assig = models.TextField(choices = assi, null = True, verbose_name = "課題重さ")
    comme = models.TextField(max_length = 50, null = True, verbose_name = "")
    contributor = models.TextField(max_length = 50, null = True, verbose_name = "投稿者")
    like = models.IntegerField(null = True, default = 0)
    date = models.TextField(null = True)

    def __str__(self):
        return self.clas


class SE(models.Model):

    clas = models.CharField(max_length = 25, verbose_name = "科目")
    semes = models.TextField(choices = sem, null = True, verbose_name = "学期")
    prof = models.CharField(max_length = 25, default = "", verbose_name = "先生")
    ease = models.TextField(choices = star, null = True, verbose_name = "楽単度")
    aplus = models.TextField(choices = star, null = True, verbose_name = "評価A以上")
    fulfil = models.TextField(choices = star, null = True, verbose_name = "内容")
    test = models.TextField(choices = tf, null = True, verbose_name = "小テスト")
    exam = models.TextField(choices = tf, null = True, verbose_name = "期末テスト")
    cheat = models.TextField(choices = ok, null = True, verbose_name = "試験レジュメ持ち込み")
    attend = models.TextField(choices = atte, null = True, verbose_name = "出席")
    presen = models.TextField(choices = tf, null = True, verbose_name = "プレゼン")
    assig = models.TextField(choices = assi, null = True, verbose_name = "課題重さ")
    comme = models.TextField(max_length = 50, null = True, verbose_name = "")
    contributor = models.TextField(max_length = 50, null = True, verbose_name = "投稿者")
    like = models.IntegerField(null = True, default = 0)
    date = models.TextField(null = True)

    def __str__(self):
        return self.clas


class SP(models.Model):

    clas = models.CharField(max_length = 25, verbose_name = "科目")
    semes = models.TextField(choices = sem, null = True, verbose_name = "学期")
    prof = models.CharField(max_length = 25, default = "", verbose_name = "先生")
    ease = models.TextField(choices = star, null = True, verbose_name = "楽単度")
    aplus = models.TextField(choices = star, null = True, verbose_name = "評価A以上")
    fulfil = models.TextField(choices = star, null = True, verbose_name = "内容")
    test = models.TextField(choices = tf, null = True, verbose_name = "小テスト")
    exam = models.TextField(choices = tf, null = True, verbose_name = "期末テスト")
    cheat = models.TextField(choices = ok, null = True, verbose_name = "試験レジュメ持ち込み")
    attend = models.TextField(choices = atte, null = True, verbose_name = "出席")
    presen = models.TextField(choices = tf, null = True, verbose_name = "プレゼン")
    assig = models.TextField(choices = assi, null = True, verbose_name = "課題重さ")
    comme = models.TextField(max_length = 50, null = True, verbose_name = "")
    contributor = models.TextField(max_length = 50, null = True, verbose_name = "投稿者")
    like = models.IntegerField(null = True, default = 0)
    date = models.TextField(null = True)

    def __str__(self):
        return self.clas


class JK(models.Model):

    clas = models.CharField(max_length = 25, verbose_name = "科目")
    semes = models.TextField(choices = sem, null = True, verbose_name = "学期")
    prof = models.CharField(max_length = 25, default = "", verbose_name = "先生")
    ease = models.TextField(choices = star, null = True, verbose_name = "楽単度")
    aplus = models.TextField(choices = star, null = True, verbose_name = "評価A以上")
    fulfil = models.TextField(choices = star, null = True, verbose_name = "内容")
    test = models.TextField(choices = tf, null = True, verbose_name = "小テスト")
    exam = models.TextField(choices = tf, null = True, verbose_name = "期末テスト")
    cheat = models.TextField(choices = ok, null = True, verbose_name = "試験レジュメ持ち込み")
    attend = models.TextField(choices = atte, null = True, verbose_name = "出席")
    presen = models.TextField(choices = tf, null = True, verbose_name = "プレゼン")
    assig = models.TextField(choices = assi, null = True, verbose_name = "課題重さ")
    comme = models.TextField(max_length = 50, null = True, verbose_name = "")
    contributor = models.TextField(max_length = 50, null = True, verbose_name = "投稿者")
    like = models.IntegerField(null = True, default = 0)
    date = models.TextField(null = True)

    def __str__(self):
        return self.clas