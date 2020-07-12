from django import forms
from .models import SK, SY, HO, SG, KY, BU, BK, KI, SO, SE, SP, JK

class SKForm(forms.ModelForm):

    class Meta:
        model = SK
        fields = (
            "clas", "semes", "prof", "ease", "aplus", "fulfil", "test", "exam",
            "cheat", "attend", "presen", "assig", "comme", "contributor", "like", "date"
        )


class SYForm(forms.ModelForm):

    class Meta:
        model = SY
        fields = (
            "clas", "semes", "prof", "ease", "aplus", "fulfil", "test", "exam",
            "cheat", "attend", "presen", "assig", "comme", "contributor", "like", "date"
        )


class HOForm(forms.ModelForm):

    class Meta:
        model = HO
        fields = (
            "clas", "semes", "prof", "ease", "aplus", "fulfil", "test", "exam",
            "cheat", "attend", "presen", "assig", "comme", "contributor", "like", "date"
        )


class SGForm(forms.ModelForm):

    class Meta:
        model = SG
        fields = (
            "clas", "semes", "prof", "ease", "aplus", "fulfil", "test", "exam",
            "cheat", "attend", "presen", "assig", "comme", "contributor", "like", "date"
        )


class KYForm(forms.ModelForm):

    class Meta:
        model = KY
        fields = (
            "clas", "semes", "prof", "ease", "aplus", "fulfil", "test", "exam",
            "cheat", "attend", "presen", "assig", "comme", "contributor", "like", "date"
        )


class BUForm(forms.ModelForm):

    class Meta:
        model = BU
        fields = (
            "clas", "semes", "prof", "ease", "aplus", "fulfil", "test", "exam",
            "cheat", "attend", "presen", "assig", "comme", "contributor", "like", "date"
        )


class BKForm(forms.ModelForm):

    class Meta:
        model = BK
        fields = (
            "clas", "semes", "prof", "ease", "aplus", "fulfil", "test", "exam",
            "cheat", "attend", "presen", "assig", "comme", "contributor", "like", "date"
        )


class KIForm(forms.ModelForm):

    class Meta:
        model = KI
        fields = (
            "clas", "semes", "prof", "ease", "aplus", "fulfil", "test", "exam",
            "cheat", "attend", "presen", "assig", "comme", "contributor", "like", "date"
        )


class SOForm(forms.ModelForm):

    class Meta:
        model = SO
        fields = (
            "clas", "semes", "prof", "ease", "aplus", "fulfil", "test", "exam",
            "cheat", "attend", "presen", "assig", "comme", "contributor", "like", "date"
        )


class SEForm(forms.ModelForm):

    class Meta:
        model = SE
        fields = (
            "clas", "semes", "prof", "ease", "aplus", "fulfil", "test", "exam",
            "cheat", "attend", "presen", "assig", "comme", "contributor", "like", "date"
        )


class SPForm(forms.ModelForm):

    class Meta:
        model = SP
        fields = (
            "clas", "semes", "prof", "ease", "aplus", "fulfil", "test", "exam",
            "cheat", "attend", "presen", "assig", "comme", "contributor", "like", "date"
        )


class JKForm(forms.ModelForm):

    class Meta:
        model = JK
        fields = (
            "clas", "semes", "prof", "ease", "aplus", "fulfil", "test", "exam",
            "cheat", "attend", "presen", "assig", "comme", "contributor", "like", "date"
        )