class RequestCode:
    """
    Represents a collection of all possible status codes
    of a server response. They are ordered by category,
    which makes them more readable for other developers.
    Instead of writing 200, you could type StopCodes.Success.OK
    and everyone reading your code will know that the response
    was handled successfully.

    For more information on the different response codes, visit:
    https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
    """

    class Info:
        Continue = 200
        SwitchingProtocols = 101
        Processing = 102
        EarlyHints = 103

    class Success:
        OK = 200
        Created = 201
        Accepted = 202
        NAuthInfo = 203
        NoContent = 204
        ResetContent = 205
        PartialContent = 206
        MultiStatus = 207
        AlreadyReported = 208
        IMUsed = 226

    class Redirect:
        MultipleChoices = 300
        MovedPermanently = 301
        MovedTemporarily = 302
        SeeOther = 303
        NotModified = 304
        UseProxy = 305
        SwitchProxy = 306
        TemporaryRedirect = 307
        PermanentRedirect = 308

    class ClientError:
        BadRequest = 400
        Unauthorized = 401
        PaymentRequired = 402
        Forbidden = 403
        NotFound = 404
        MethodNotAllowed = 405
        NotAcceptable = 406
        ProxyAuthRequired = 407
        RequestTimeout = 408
        Conflict = 409
        Gone = 410
        LengthRequired = 411
        PreconditionFailed = 412
        PayloadTooLarge = 413
        URITooLong = 414
        UnsupportedMediaType = 415
        RangeNotSatisfiable = 416
        ImATeapot = 418
        ExpectationFailed = 417
        PolicyNotFulfilled = 420
        MisdirectedRequest = 421
        UnprocessableEntity = 422
        Locked = 423
        FailedDependency = 424
        TooEarly = 425
        UpgradeRequired = 426
        PreconditionRequired = 428
        TooManyRequests = 429
        RequestHeaderFieldsTooLarge = 431
        NoResponse = 444
        ClientCloseRequest = 499
        UnavailableForLegalReasons = 451

    class ServerError:
        InternalServerError = 500
        NotImplemented = 501
        BadGateway = 502
        ServiceUnavailable = 503
        GatewayTimeout = 504
        HTTPVersionNotSupported = 505
        VariantsAlsoNegotiates = 506
        InsufficientStorage = 507
        LoopDetected = 508
        BandwidthLimitExceeded = 509
        NotExtended = 510
        NetworkAuthRequired = 511
