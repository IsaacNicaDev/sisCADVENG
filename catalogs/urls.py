from rest_framework import routers

from .api import GenderViewSet
from .api import GradeViewSet
from .api import SubjectViewSet
from .api import MunicipalityViewSet
from .api import EducationalLevelViewSet
from .api import ModalityViewSet
from .api import SectionViewSet
from .api import ShiftViewSet
from .api import EducationalInstitutionViewSet
from .api import EnrolmentTypeViewSet
from .api import CityViewSet
from .api import CountryViewSet
from .api import LanguageViewSet
from .api import EthnicityViewSet
from .api import DisabilityViewSet
from .api import ReligionViewSet
from .api import DepartamentViewSet
from .api import DepartamentalDelegationViewSet
from .api import ZoneViewSet
from .api import DistrictViewSet
from .api import MaritalStatusViewSet

router = routers.DefaultRouter()

router.register('genders', GenderViewSet, 'genders'),
router.register('grades', GradeViewSet, 'grades')
router.register('subjects', SubjectViewSet, 'subjects')
router.register('municipalities', MunicipalityViewSet, 'municipalities')
router.register('educational-levels', EducationalLevelViewSet, 'educational-levels')
router.register('modalities', ModalityViewSet, 'modalities')
router.register('sections', SectionViewSet, 'sections')
router.register('shifts', ShiftViewSet, 'shifts')
router.register('educational-institutions', EducationalInstitutionViewSet, 'educational-institutions')
router.register('enrolment-types', EnrolmentTypeViewSet, 'enrolment-types')
router.register('cities', CityViewSet, 'cities')
router.register('countries', CountryViewSet, 'countries')
router.register('languages', LanguageViewSet, 'languages')
router.register('ethnicities', EthnicityViewSet, 'ethnicities')
router.register('disabilities', DisabilityViewSet, 'disabilities')
router.register('religions', ReligionViewSet, 'religions')
router.register('departaments', DepartamentViewSet, 'departaments')
router.register('departamental-delegations', DepartamentalDelegationViewSet, 'departamental-delegations')
router.register('zones', ZoneViewSet, 'zones')
router.register('districts', DistrictViewSet, 'districts')
router.register('maritalstatus', MaritalStatusViewSet, 'maritalstatus')

urlpatterns = router.urls