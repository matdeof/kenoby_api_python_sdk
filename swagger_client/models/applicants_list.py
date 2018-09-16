
from pprint import pformat
from six import iteritems


class ApplicantsList(object):
    """
    This class represents the data model used in ApplicantsApi
    
    """

    def __init__(self):
        """
        ApplicantsList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'averageMappingsScore': 'number',
            'hasReferralInternal': 'bool',
            'updatedAt': 'str',
            'code': 'number',
            'email': 'str',
            'user': 'str',
            'name': 'str',
            'createdAt': 'str',
            'tenant': 'str',
            'waitingApproval': 'list(str)',
            'deleted': 'bool',
            'referralInternal': 'list(str)',
            'evaluationAverage': 'number',
            'ratingAverage': 'number',
            'files': 'list(str)'
        }

        self.attribute_map = {
        	'id': 'id',
            'averageMappingsScore': 'averageMappingsScore',
            'hasReferralInternal': 'hasReferralInternal',
            'updatedAt': 'updatedAt',
            'code': 'code',
            'email': 'email',
            'user': 'user',
            'name': 'name',
            'createdAt': 'createdAt',
            'tenant': 'tenant',
            'waitingApproval': 'waitingApproval',
            'deleted': 'deleted',
            'referralInternal': 'referralInternal',
            'evaluationAverage': 'evaluationAverage',
            'ratingAverage': 'ratingAverage',
            'files': 'files'
        }


        self._id = None

        self._averageMappingsScore = None

        self._hasReferralInternal = None

        self._updatedAt = None

        self._code = None

        self._email = None

        self._user = None

        self._name = None

        self._createdAt = None

        self._tenant = None

        self._waitingApproval = None

        self._deleted = None

        self._referralInternal = None

        self._evaluationAverage = None

        self._ratingAverage = None

        self._files = None




    @property
    def id(self):
        """
        Gets the id of Applicant.
        ID of Applicants

        :return: The id of Applicant.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of Applicant.
        ID of Applicants

        :param id: The id of Applicant.
        :type: str
        """
        self._id = id

    @property
    def averageMappingsScore(self):
        """
        Gets the averageMappingsScore of Applicant.
        averageMappingsScore of Applicants

        :return: The averageMappingsScore of Applicant.
        :rtype: number
        """
        return self._id

    @averageMappingsScore.setter
    def averageMappingsScore(self, averageMappingsScore):
        """
        Sets the averageMappingsScore of Applicant.
        averageMappingsScore of Applicants

        :param averageMappingsScore: The averageMappingsScore of Applicant.
        :type: number
        """
        self._averageMappingsScore = averageMappingsScore

    @property
    def hasReferralInternal(self):
        """
        Gets the hasReferralInternal of Applicant.
        hasReferralInternal of Applicants

        :return: Wether Applicant hasReferralInternal.
        :rtype: bool
        """
        return self._hasReferralInternal

    @hasReferralInternal.setter
    def hasReferralInternal(self, hasReferralInternal):
        """
        Sets whether Applicant hasReferralInternal.
        Whether Applicant hasReferralInternal

        :param hasReferralInternal: The averageMappingsScore of Applicant.
        :type: bool
        """
        self._hasReferralInternal = hasReferralInternal


    @property
    def updatedAt(self):
        """
        Gets the updatedAt of Applicant.
        updatedAt of Applicants

        :return: The updatedAt of Applicant.
        :rtype: str
        """
        return self._updatedAt

    @updatedAt.setter
    def updatedAt(self, updatedAt):
        """
        Sets the updatedAt of Applicant.
        updatedAt of Applicants

        :param updatedAt: The updatedAt of Applicant.
        :type: str
        """
        self._updatedAt = updatedAt

    @property
    def code(self):
        """
        Gets the code of Applicant.
        code of Applicants

        :return: The code of Applicant.
        :rtype: number
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of Applicant.
        code of Applicants

        :param code: The code of Applicant.
        :type: number
        """
        self._code = code

    @property
    def email(self):
        """
        Gets the email of Applicant.
        email of Applicants

        :return: The email of Applicant.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of Applicant.
        email of Applicants

        :param email: The email of Applicant.
        :type: str
        """
        self._email = email

    @property
    def user(self):
        """
        Gets the user of Applicant.
        user of Applicants

        :return: The user of Applicant.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of Applicant.
        user of Applicants

        :param user: The user of Applicant.
        :type: str
        """
        self._user = user

    @property
    def createdAt(self):
        """
        Gets the createdAt of Applicant.
        createdAt of Applicants

        :return: The createdAt of Applicant.
        :rtype: str
        """
        return self._createdAt

    @createdAt.setter
    def createdAt(self, createdAt):
        """
        Sets the createdAt of Applicant.
        createdAt of Applicants

        :param createdAt: The createdAt of Applicant.
        :type: str
        """
        self._createdAt = createdAt

    @property
    def tenant(self):
        """
        Gets the tenant of Applicant.
        tenant of Applicants

        :return: The tenant of Applicant.
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """
        Sets the tenant of Applicant.
        tenant of Applicants

        :param tenant: The tenant of Applicant.
        :type: str
        """
        self._tenant = tenant

    @property
    def waitingApproval(self):
        """
        Gets the waitingApproval of Applicant.
        waitingApproval of Applicants

        :return: The waitingApproval of Applicant.
        :rtype: list
        """
        return self._waitingApproval

    @waitingApproval.setter
    def waitingApproval(self, waitingApproval):
        """
        Sets the waitingApproval of Applicant.
        waitingApproval of Applicants

        :param waitingApproval: The waitingApproval of Applicant.
        :type: list
        """
        self._waitingApproval = waitingApproval

    @property
    def deleted(self):
        """
        Gets the deleted of Applicant.
        deleted of Applicants

        :return: The deleted of Applicant.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of Applicant.
        deleted of Applicants

        :param deleted: The deleted of Applicant.
        :type: bool
        """
        self._deleted = deleted

    @property
    def referralInternal(self):
        """
        Gets the referralInternal of Applicant.
        referralInternal of Applicants

        :return: The referralInternal of Applicant.
        :rtype: list
        """
        return self._referralInternal

    @referralInternal.setter
    def referralInternal(self, referralInternal):
        """
        Sets the referralInternal of Applicant.
        referralInternal of Applicants

        :param referralInternal: The referralInternal of Applicant.
        :type: list
        """
        self._referralInternal = referralInternal

    @property
    def evaluationAverage(self):
        """
        Gets the evaluationAverage of Applicant.
        evaluationAverage of Applicants

        :return: The evaluationAverage of Applicant.
        :rtype: number
        """
        return self._evaluationAverage

    @evaluationAverage.setter
    def evaluationAverage(self, evaluationAverage):
        """
        Sets the evaluationAverage of Applicant.
        evaluationAverage of Applicants

        :param evaluationAverage: The evaluationAverage of Applicant.
        :type: number
        """
        self._evaluationAverage = evaluationAverage

    @property
    def files(self):
        """
        Gets the files of Applicant.
        files of Applicants

        :return: The files of Applicant.
        :rtype: list
        """
        return self._files

    @files.setter
    def files(self, files):
        """
        Sets the files of Applicant.
        files of Applicants

        :param files: The files of Applicant.
        :type: list
        """
        self._files = files

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other



